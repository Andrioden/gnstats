function VerificationDialogController($rootScope, $scope, $mdDialog, $http, $window) {

    // CONSTRUCTOR
    $scope.availableUserNames = undefined;
    $scope.submitting = false;

    $http.get('/api/users/available-names/').
        then(function(response) {
            $scope.availableUserNames = response.data;
        }, function(response) {
            alertError(response);
        });

    // PUBLIC METHODS

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.verify = function() {
        $scope.submitting = true;

        $http.post('/api/users/me/verify/', {name: $rootScope.user.name}, {}).
            then(function() {
                $scope.submitting = false;
                $rootScope.user.registered = true;
                $mdDialog.cancel();
                $window.location.reload();
            }, function(response) {
                $scope.submitting = false;
                alertError(response);
            });
    }

    // PRIVATE METHODS

    console.log("VerificationDialogController loaded");

}