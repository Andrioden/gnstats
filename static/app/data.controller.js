app.controller('DataController', function($rootScope, $scope, $http, $window, $mdDialog){

    // *************** PUBLIC VARIABLES ***************

    $scope.gameNights;
    $scope.sortingBy = "";
    $scope.showingSearch = false;
    $scope.search = "";

    $scope.loadingData = false;


    // *************** CONSTRUCTOR ***************



    // *************** TRIGGER METHODS ***************

    $rootScope.$on('openGameNightDialog', function (event, args) { $scope.openGameNightDialog(args.ev, args.gameNight); });
    $rootScope.$on('loadGameNights', function (event, args) { loadGameNights(); });


    // *************** PUBLIC METHODS ***************

    $scope.openGameNightDialog = function (ev, gameNight) {
        $mdDialog.show({
            controller: GameNightDialogController,
            templateUrl: 'static/app/data-extra.gameNightDialog.template.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true,
            fullscreen: $scope.customFullscreen, // Only for -xs, -sm breakpoints.
            locals: { gameNight: gameNight },
        })
        // Hidden with potential return value
        .then(function(dialogResponse) {
            if (dialogResponse.reloadGameNights == true)
                loadGameNights();
        },
        // Cancelled
        function(){});
    };

    $scope.addNewGameNightRow = function() {
        $scope.gameNights.push({
            date: new Date(),
            sum: "vote",
            votes: (function(){
                var votes = [];
                for(var i=0; i < $rootScope.persons.length; i++) {
                    if ($rootScope.persons[i].activated) {
                        votes.push({
                            voter: $rootScope.persons[i].name,
                        });
                    }
                }
                return votes;
            })()
        });
        $scope.sortByDate();
    }

    $scope.sortByDate = function () {
        $scope.showingSearch = false;
        $scope.gameNights.sort(function(a, b){return b.date-a.date;});
        $scope.sortingBy = "Sort:Date";
    }

    $scope.sortByHost = function () {
        $scope.showingSearch = false;
        $scope.gameNights.sort(function(a, b){ return a.host.localeCompare(b.host); });
        $scope.sortingBy = "Sort:Host";
    }

    $scope.sortByTotalRating = function () {
        $scope.showingSearch = false;
        $scope.gameNights.sort(function(a, b){ return b.sum-a.sum; });
        $scope.sortingBy = "Sort:Total";
    }

    $scope.sortByOwnRating = function () {
        $scope.showingSearch = false;
        $scope.gameNights.sort(function(a, b){
            if (!a.own_vote)
                return 1;
            else if (!b.own_vote)
                return -1;
            else
                return b.own_vote.sum-a.own_vote.sum;
        });
        $scope.sortingBy = "Sort:Own";
    }

    $scope.sortByTotalVotePartRating = function (part) {
        $scope.showingSearch = false;
        $scope.gameNights.sort(function (a, b) { return summarizeVotesRatingPart(b, part) - summarizeVotesRatingPart(a, part); });
        $scope.sortingBy = "Sort:TotalVotePart";
    }

    $scope.showSearch = function () {
        $scope.showingSearch = true;
    }

    // Source: http://stackoverflow.com/questions/11753321/passing-arguments-to-angularjs-filters/
    $scope.customFilter = function (search) {
        search = search.toLowerCase();
        return function (gameNight) {
            if (search == "" || search == undefined)
                return true;
            if (gameNight.host.toLowerCase().indexOf(search) > -1)
                return true;
            if (gameNight.description.toLowerCase().indexOf(search) > -1)
                return true;
            if (gameNight.searchMetaData.toLowerCase().indexOf(search) > -1)
                return true;

            return false;
        }
    }

    $scope.personIdFromName = function (name) {
        var host = $rootScope.persons.find(x => x.name === name && x.id !== 'undefined');
        if (typeof host !== "undefined")
            return host.id;
    }


    // *************** PRIVATE METHODS ***************

    function loadGameNights() {
        $scope.loadingData = true;

        $http.get('/api/game_night/').
            then(function(response) {
                $scope.loadingData = false;
                $scope.gameNights = response.data;
                loadedGameNightsProcessing();
            }, function(response) {
                $scope.loadingData = false;
                alertError(response);
            });
    }

    function loadedGameNightsProcessing() {
        setGameNightDates($scope.gameNights);
        setGameNightVoteStatus($scope.gameNights);
        setGameNightLastOfRounds($scope.gameNights);
        addSearchableMetaData($scope.gameNights);
        $scope.sortByDate();
    }

    function setGameNightDates(gameNights) {
        for(var i=0; i<gameNights.length; i++) {
            if (gameNights[i].date_epoch)
                gameNights[i].date = new Date(gameNights[i].date_epoch * 1000);
            else
                gameNights[i].date = null;
        }
    }

    function setGameNightVoteStatus(gameNights) {
        for(var i=0; i<gameNights.length; i++) {
            if (gameNights[i].own_vote && !gameNights[i].own_vote.complete_vote && gameNights[i].host != $rootScope.user.name)
                gameNights[i].voteStatus = "red";
            else if (gameNights[i].votes.length < 3)
                gameNights[i].voteStatus = "orange";
            else
                gameNights[i].voteStatus = "";
        }
    }

    function setGameNightLastOfRounds(gameNights) {
        // Ascending sort
        gameNights.sort(function(a, b){return a.date-b.date;});

        // Offset by 1 since we have to pretend the game night before first game night was the previous one, for this algorithm to work.
        var previousIsLastOfRoundIndex = -1;

        for(var i=0; i<gameNights.length; i++) {
            var gameNightsSinceLastFirstOfRoundCount = i - previousIsLastOfRoundIndex;
            var peoplePartOfRound = gameNights[i].votes.length + 1; // +1 because host do not vote

            if (gameNightsSinceLastFirstOfRoundCount == peoplePartOfRound) {
                gameNights[i].isLastOfRound = true;
                previousIsLastOfRoundIndex = i;
            }
        }
    }

    function addSearchableMetaData(gameNights) {
        for(var i=0; i<gameNights.length; i++) {
            gameNights[i].searchMetaData = "h:" + gameNights[i].host;
            if (gameNights[i].date)
                gameNights[i].searchMetaData += " " + moment(gameNights[i].date).format("DD/MM/YYYY");
        }
    }

    function summarizeVotesRatingPart(gameNight, part) {
        var sum = 0;

        for (var i = 0; i < gameNight.votes.length; i++)
            if (!isNaN(gameNight.votes[i][part]))
                sum += gameNight.votes[i][part];

        return sum;
    }

    loadGameNights();

    console.log("DataController loaded");
});