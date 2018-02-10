function VerificationDialogController($rootScope, $scope, $mdDialog, $http, $window) {

    // CONSTRUCTOR

    $scope.availablePersonNames;
    $scope.password = "";

    $scope.submitting = false;

    $http.get('/api/users/available-names/').
        then(function(response) {
            $scope.availablePersonNames = response.data;
        }, function(response) {
            alertError(response);
        });

    // PUBLIC METHODS

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.verify = function() {
        $scope.submitting = true;

        $http.post('/api/users/me/verify/', {name: $rootScope.user.name, password: $scope.password}, {}).
            then(function(response) {
                $scope.submitting = false;
                $rootScope.user.verified = true;
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