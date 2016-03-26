app.controller('DataController', function($rootScope, $scope, $http, $window){

    // *************** PUBLIC VARIABLES ***************

    $scope.personNames = ['Stian', 'André', 'Ole', 'Damian'];
    $scope.gameNights = [];
    $scope.showLandscapeWarning = false;
    $scope.sortByText = "";


    // *************** CONSTRUCTOR ***************
    $('[data-toggle="popover"]').popover()

    loadGameNightData();

    hideOrShowLandscapeWarning();

    $(window).resize(function(){
        $scope.$apply(function(){
            hideOrShowLandscapeWarning();
        });
    });

    console.log("DataController loaded")

    // *************** PUBLIC METHODS ***************

    $scope.addNewGameNightRow = function() {
        $scope.gameNights.push({
            date: new Date(),
            sum: "vote",
            votes: (function(){
                var votes = [];
                for(var i=0; i<$scope.personNames.length; i++) {
                    votes.push({
                        voter: $scope.personNames[i],
                    });
                }
                return votes;
            })()
        });
        $scope.sortByDate();
    }

    $scope.isSaving = false;

    $scope.save = function() {
        $scope.isSaving = true;
        var changedGameNights = findChangedGameNights();

        if (changedGameNights.length > 0) {
            $http.put('/api/game_night/sync', changedGameNights, {}).
                then(function(response) {
                    $scope.isSaving = false;
                    loadGameNightData();
                }, function(response) {
                    alertError(response);
                    $scope.isSaving = false;
                });
        }
        else {
            console.log("No games to save");
            $scope.isSaving = false;
        }
    }

    $scope.deleteGameNight = function(gameNight) {
        $http.delete('/api/game_night/' + gameNight.id).
            then(function(response) {
                loadGameNightData();
            }, function(response) {
                alertError(response);
            });
    }

    $scope.sortByDate = function() {
        $scope.gameNights.sort(function(a, b){return b.date-a.date;});
        $scope.sortByText = "Sort:Date";
    }

    $scope.sortByHost = function() {
        $scope.gameNights.sort(function(a, b){ return a.host.localeCompare(b.host); });
        $scope.sortByText = "Sort:Host";
    }

    $scope.sortByTotalRating = function() {
        $scope.gameNights.sort(function(a, b){ return b.sum-a.sum; });
        $scope.sortByText = "Sort:Total";
    }

    $scope.sortByOwnRating = function() {
        $scope.gameNights.sort(function(a, b){
            if (!a.own_vote)
                return 1;
            else if (!b.own_vote)
                return -1;
            else
                return b.own_vote.sum-a.own_vote.sum;
        });
        $scope.sortByText = "Sort:Own";
    }

    // Source: http://stackoverflow.com/questions/11753321/passing-arguments-to-angularjs-filters/
    $scope.customFilter = function(search) {
        return function(gameNight) {
            if (search == "" || search == undefined)
                return true;
            if (gameNight.host.indexOf(search) > -1)
                return true;
            if (gameNight.description.indexOf(search) > -1)
                return true;
            if (gameNight.searchMetaData.indexOf(search) > -1)
                return true;

            return false;
        }
    }

    // *************** PRIVATE METHODS ***************

    function loadGameNightData() {
        $http.get('/api/game_night/').
            then(function(response) {
                $scope.gameNights = response.data
                setGameNightDates($scope.gameNights);
                setGameNightBackgroundColorClasses($scope.gameNights);
                $scope.sortByDate();
                addSearchableMetaData($scope.gameNights);
            }, function(response) {
                alertError(response);
            });
    }

    function findChangedGameNights() {
        var changedGameNights = [];
        $("#dataView").find('.ng-dirty').closest('.game-night').each(function( index ) {
            var id = $(this).attr('id');
            var idIndex = parseInt(id.split("_")[1]);
            var gameNight = $scope.gameNights[idIndex];
            gameNight.index = idIndex;
            changedGameNights.push(gameNight);
        });
        return changedGameNights;
    }

    function setGameNightDates(gameNights) {
        for(var i=0; i<gameNights.length; i++) {
            if (gameNights[i].date_epoch)
                gameNights[i].date = new Date(gameNights[i].date_epoch * 1000);
            else
                gameNights[i].date = null;
        }
    }

    function setGameNightBackgroundColorClasses(gameNights) {
        for(var i=0; i<gameNights.length; i++) {
            gameNights[i].backgroundColorClass = backgroundColorClass(gameNights[i]);
        }
    }

    function addSearchableMetaData(gameNights) {
        for(var i=0; i<gameNights.length; i++) {
            gameNights[i].searchMetaData = "h:" + gameNights[i].host;
            if (gameNights[i].date)
                gameNights[i].searchMetaData += " " + gameNights[i].date.yyyy_mm_dd();
        }
    }

    function backgroundColorClass(gameNight) {
        if (gameNight.own_vote && !gameNight.own_vote.complete_vote && gameNight.host != $rootScope.user.name)
            return "red-background";
        else if (gameNight.votes.length != 3)
            return "orange-background";
        else
            return "";
    }

    function hideOrShowLandscapeWarning() {
        $scope.showLandscapeWarning = $window.innerHeight > $window.innerWidth;
    }

});