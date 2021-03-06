function AdminDialogController($rootScope, $scope, $mdDialog, $http) {

    // *************** PUBLIC VARIABLES ***************

    $scope.submitting = false;

    // *************** CONSTRUCTOR ***************


    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.updateActivated = function (person, newActivated) {
        $scope.submitting = true;

        $http.put('/api/users/' + person.id + '/', { activated: newActivated}, {}).
            then(function (response) {
                $scope.submitting = false;
                person.activated = newActivated;
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.recalcGameNightSums = function () {
        $scope.submitting = true;

        $http.post('/api/actions/admin/recalculategnsums/', {}).
            then(function (response) {
                $scope.submitting = false;
                $rootScope.$emit('loadGameNights');
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    // *************** PRIVATE METHODS ***************


    console.log("AdminDialogController loaded");
}