app.controller('DataController', function($rootScope, $scope, $http, $window, $mdDialog){

    // *************** PUBLIC VARIABLES ***************

    $scope.gameNights = [];
    $scope.sortingBy = "";
    $scope.showingSearch = false;
    $scope.search = "";

    $scope.loadingData = false;


    // *************** CONSTRUCTOR ***************



    // *************** TRIGGER METHODS ***************

    $rootScope.$on('openGameNightDialog', function (event, args) { $scope.openGameNightDialog(args.ev, args.gameNight); });
    $rootScope.$on('loadGameNights', function () { loadGameNights(); });


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
            if (dialogResponse.created)
                addLocalGameNight(dialogResponse.created);
            if (dialogResponse.updated)
                updateLocalGameNight(dialogResponse.updated)
            if (dialogResponse.deleted)
                deleteLocalGameNight(dialogResponse.deleted);
        },
        // Cancelled
        function(){});
    };

    $scope.addNewGameNightRow = function() {
        $scope.gameNights.push({
            date: new Date(),
            sum: "vote",
            votes: (function(){
                let votes = [];
                for(let i=0; i < $rootScope.users.length; i++) {
                    if ($rootScope.users[i].activated) {
                        votes.push({
                            voter: $rootScope.users[i].name,
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
            if (search === "" || search === undefined)
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

    $scope.pictureUrl = function (name) {
        let host = $rootScope.users.find(x => x.name === name && x.id !== 'undefined');
        if (typeof host !== "undefined" && host.picture_url)
            return host.picture_url;
        else
            return "";
    }


    // *************** PRIVATE METHODS ***************

    function loadGameNights() {
        $scope.loadingData = true;
        $http.get('/api/gamenights/').
            then(function(response) {
                $scope.loadingData = false;
                $scope.gameNights = response.data;
                loadedGameNightsProcessing();
            }, function(response) {
                $scope.loadingData = false;
                alertError(response);
            });
    }

    function addLocalGameNight(gameNight) {
        $scope.gameNights.push(gameNight);
        loadedGameNightsProcessing();
    }

    function updateLocalGameNight(gameNight) {
        for (let i = 0; i < $scope.gameNights.length; i++) {
            if ($scope.gameNights[i].id === gameNight.id) {
                $scope.gameNights[i] = gameNight;
                loadedGameNightsProcessing();
                return;
            }
        }

        throw "Local game night '" + gameNight.id + "' does not exist";
    }

    function deleteLocalGameNight(gameNightId) {
        let index = $scope.gameNights.findIndex(x => x.id === gameNightId);
        $scope.gameNights.splice(index, 1);
        loadedGameNightsProcessing();
    }

    function loadedGameNightsProcessing() {
        setGameNightDates($scope.gameNights);
        setGameNightVoteStatus($scope.gameNights);
        addSearchableMetaData($scope.gameNights);
        $scope.sortByDate();
    }

    function setGameNightDates(gameNights) {
        for(let i=0; i<gameNights.length; i++) {
            if (gameNights[i].date_epoch)
                gameNights[i].date = new Date(gameNights[i].date_epoch * 1000);
            else
                gameNights[i].date = null;
        }
    }

    function setGameNightVoteStatus(gameNights) {
        for(let i=0; i<gameNights.length; i++) {
            if (gameNights[i].own_vote && !gameNights[i].own_vote.completed_vote && gameNights[i].host !== $rootScope.user.name)
                gameNights[i].voteStatus = "red";
            else if (gameNights[i].votes.length < 3)
                gameNights[i].voteStatus = "orange";
            else
                gameNights[i].voteStatus = "";
        }
    }

    function addSearchableMetaData(gameNights) {
        for(let i=0; i<gameNights.length; i++) {
            gameNights[i].searchMetaData = "h:" + gameNights[i].host;
            if (gameNights[i].date)
                gameNights[i].searchMetaData += " " + moment(gameNights[i].date).format("DD/MM/YYYY");
        }
    }

    function summarizeVotesRatingPart(gameNight, part) {
        let sum = 0;

        for (let i = 0; i < gameNight.votes.length; i++)
            if (!isNaN(gameNight.votes[i][part]))
                sum += gameNight.votes[i][part];

        return sum;
    }

    loadGameNights();

    console.log("DataController loaded");
});