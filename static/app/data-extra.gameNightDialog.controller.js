function GameNightDialogController($rootScope, $scope, $mdDialog, $http, gameNight) {

    // *************** PUBLIC VARIABLES ***************

    $scope.submitting = false;


    // *************** CONSTRUCTOR ***************
    $scope.gameNight = gameNight;
    if ($scope.gameNight === null)
        $scope.gameNight = createNewLocalGameNightObject();

    var host = $rootScope.persons.find(x => x.name === $scope.gameNight.host && x.id !== 'undefined');
    if (typeof host !== "undefined")
        $scope.hostId = host.id;

    //console.log($scope.gameNight);

    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.create = function() {
        $scope.submitting = true;

        $http.post('/api/game_night/', $scope.gameNight, {}).
            // Success
            then(function(response) {
                $scope.submitting = false;
                $mdDialog.hide({ reloadGameNights: true });
            // Error
            }, function(response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.save = function () {
        $scope.submitting = true;

        $http.put('/api/game_night/' + $scope.gameNight.id + "/", $scope.gameNight, {}).
            // Success
            then(function (response) {
                $scope.submitting = false;
                $mdDialog.hide({ reloadGameNights: true });
                // Error
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.delete = function() {
        if (confirm("Do you want to delete: " + $scope.gameNight.description)) {
            $http.delete('/api/game_night/' + $scope.gameNight.id + "/").
                // Success
                then(function (response) {
                    $mdDialog.hide({ reloadGameNights: true });
                // Error
                }, function(response) {
                    alertError(response);
                });
        }
    }

    // Currently needed because gameNight.host reference is name which has special chars. Which fails when <md-option ng-value="André">.
    // So this is a workaround that used host_id
    $scope.setGameNightHostValue = function() {
        $scope.gameNight.host = $rootScope.persons.find(x => x.id === $scope.hostId).name;
    }


    // *************** PRIVATE METHODS ***************

    function createNewLocalGameNightObject() {
        return {
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
        };
    }

    console.log("GameNightDialogController loaded for object 0" + $scope.gameNight.id);

}