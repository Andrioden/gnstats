function AdminDialogController($rootScope, $scope, $mdDialog, $http) {

    // *************** PUBLIC VARIABLES ***************

    $scope.submitting = false;

    // *************** CONSTRUCTOR ***************


    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    $scope.updateActivated = function (user, newActivated) {
        $scope.submitting = true;

        $http.put('/api/users/' + user.id + '/', { activated: newActivated}, {}).
            then(function () {
                $scope.submitting = false;
                user.activated = newActivated;
            }, function (response) {
                $scope.submitting = false;
                alertError(response);
            });
    };

    $scope.recalcGameNightSums = function () {
        $scope.submitting = true;

        $http.post('/api/actions/admin/recalculategnsums/', {}).
            then(function () {
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