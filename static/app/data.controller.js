app.controller('DataController', function($rootScope, $scope, $http){

    // *************** PUBLIC VARIABLES ***************

    $scope.persons = ['Stian', 'André', 'Ole', 'Damian'];
    $scope.gameNights = [];


    // *************** CONSTRUCTOR ***************

    console.log("DataController loaded")

    loadGameNights();


    // *************** PUBLIC METHODS ***************

    $scope.addNewGameNightRow = function() {
        $scope.gameNights.push({
            date: new Date(),
            sum: "vote",
            votes: (function(){
                var votes = [];
                for(var i=0; i<$scope.persons.length; i++) {
                    votes.push({
                        voter: $scope.persons[i],
                    });
                }
                return votes;
            })()
        });
        sortByDate();
    }

    $scope.save = function() {
        var changedGameNights = findChangedGameNights();

        if (changedGameNights.length > 0) {
            $http.put('/api/game_night/sync', changedGameNights, {}).
                then(function(response) {
                    for(var i=0; i<response.data.length; i++) {
                        $scope.gameNights[response.data[i].index].id = response.data[i].id;
                        $scope.gameNights[response.data[i].index].sum = response.data[i].sum;
                    }
                }, function(response) {
                    alertError(response);
                });
        }
        else {
            console.log("No games to save");
        }
    }


    // *************** PRIVATE METHODS ***************

    function loadGameNights() {
        $http.get('/api/game_night/').
            then(function(response) {
                $scope.gameNights = response.data
                setGameNightDates($scope.gameNights);
                sortByDate();
            }, function(response) {
                alertError(response);
            });
    }

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
            gameNights[i].date = new Date(gameNights[i].date_epoch * 1000);
        }
    }


});