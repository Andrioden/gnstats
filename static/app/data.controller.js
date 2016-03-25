app.controller('DataController', function($rootScope, $scope, $http, $window){

    // *************** PUBLIC VARIABLES ***************

    $scope.personNames = ['Stian', 'André', 'Ole', 'Damian'];
    $scope.gameNights = [];
    $scope.showLandscapeWarning = false;


    // *************** CONSTRUCTOR ***************

    console.log("DataController loaded")

    $http.get('/api/game_night/').
        then(function(response) {
            $scope.gameNights = response.data
            setGameNightDates($scope.gameNights);
            setGameNightBackgroundColorClasses($scope.gameNights);
            sortByDate();
        }, function(response) {
            alertError(response);
        });

    hideOrShowLandscapeWarning();

    $(window).resize(function(){
        $scope.$apply(function(){
            hideOrShowLandscapeWarning();
        });
    });


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
        sortByDate();
    }

    $scope.isSaving = false;

    $scope.save = function() {
        $scope.isSaving = true;
        var changedGameNights = findChangedGameNights();

        if (changedGameNights.length > 0) {
            $http.put('/api/game_night/sync', changedGameNights, {}).
                then(function(response) {
                    for(var i=0; i<response.data.length; i++) {
                        var localGameNightObject = $scope.gameNights[response.data[i].index];
                        localGameNightObject.id = response.data[i].id;
                        localGameNightObject.sum = response.data[i].sum;
                        localGameNightObject.votes = response.data[i].votes;
                        localGameNightObject.own_vote = response.data[i].own_vote;
                        localGameNightObject.completely_voted = response.data[i].completely_voted;
                        localGameNightObject.backgroundColorClass = backgroundColorClass(localGameNightObject);
                    }
                    $scope.isSaving = false;
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




    // *************** PRIVATE METHODS ***************

    function sortByDate() {
        $scope.gameNights.sort(function(a, b){return b.date-a.date;});
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

    function backgroundColorClass(gameNight) {
        if (!gameNight.own_vote.complete_vote && gameNight.host != $rootScope.user.name)
            return "red-background";
        else if (!gameNight.completely_voted)
            return "orange-background";
        else
            return "";
    }

    function hideOrShowLandscapeWarning() {
        $scope.showLandscapeWarning = $window.innerHeight > $window.innerWidth;
    }

});