app.controller('DataController', function($rootScope, $scope, $http){

    console.log("DataController loaded")

    // PUBLIC VARIABLES

    $scope.persons = ['Stian', 'André', 'Ole', 'Damian'];
    $scope.gameNights = [];

    // PUBLIC METHODS

    $scope.addNewGameNightRow = function() {
        $scope.gameNights.push({
            id: null,
            host: null,
            date: null,
            description: "",
            sum: 1,
            voters: (function(){
                var voters = [];
                for(var i=0; i<$scope.persons.length; i++) {
                    voters.push({
                        name: $scope.persons[i],
                        appetizer: "",
                        main_course: "",
                        dessert: "",
                        game: "",
                    });
                }
                return voters;
            })()
        });
    }

    $scope.addNewGameNightRow();

    $scope.save = function() {
        var changedGameNights = findChangedGameNights();
        console.log(changedGameNights);

        if (changedGameNights.length > 0) {
            $http.put('/api/game_night/sync', findChangedGameNights(), {}).
                then(function(response) {
                    console.log("OK")
                }, function(response) {
                    alertError(response);
                });
        }
        else {
            console.log("No games saved");
        }
    }


    // PRIVATE METHODS

    function findChangedGameNights() {
        var changedGameNights = [];
        $("#dataView").find('.ng-dirty').closest('.game-night').each(function( index ) {
            var id = $(this).attr('id');
            var idIndex = parseInt(id.split("_")[1]);
            changedGameNights.push($scope.gameNights[idIndex]);
        });
        return changedGameNights;
    }



});