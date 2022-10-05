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

    console.log($scope.gameNight);

    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.create = function() {
        $scope.submitting = true;
        $scope.gameNight.date = moment($scope.gameNight.date).format("YYYY-MM-DD");

        $http.post('/api/gamenights/', $scope.gameNight, {}).
            // Success
            then(function(response) {
                $scope.submitting = false;
                $mdDialog.hide({ created: response.data });
            // Error
            }, function(response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.save = function () {
        $scope.submitting = true;
        $scope.gameNight.date = moment($scope.gameNight.date).format("YYYY-MM-DD");

        $http.put('/api/gamenights/' + $scope.gameNight.id + "/", $scope.gameNight, {}).
            // Success
            then(function (response) {
                $scope.submitting = false;
                $mdDialog.hide({ updated: response.data });
                // Error
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.delete = function() {
        if (confirm("Do you want to delete: " + $scope.gameNight.description)) {
            $http.delete('/api/gamenights/' + $scope.gameNight.id + "/").
                // Success
                then(function (response) {
                    $mdDialog.hide({ deleted: $scope.gameNight.id });
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
                            present: true
                        });
                    }
                }
                return votes;
            })()
        };
    }

    console.log("GameNightDialogController loaded for object " + $scope.gameNight.id);
}