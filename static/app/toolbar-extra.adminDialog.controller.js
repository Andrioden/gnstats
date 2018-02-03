function AdminDialogController($rootScope, $scope, $mdDialog, $http) {

    // *************** PUBLIC VARIABLES ***************

    $scope.submitting = false;

    // *************** CONSTRUCTOR ***************


    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.activate = function (person) {
        $scope.submitting = true;

        $http.post('/api/users/activate/', { name: person.name }, {}).
            then(function (response) {
                $scope.submitting = false;
                person.activated = true;
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.deactivate = function (person) {
        $scope.submitting = true;

        $http.post('/api/users/deactivate/', { name: person.name }, {}).
            then(function (response) {
                $scope.submitting = false;
                person.activated = false;
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    // *************** PRIVATE METHODS ***************



    console.log("AdminDialogController loaded");
}