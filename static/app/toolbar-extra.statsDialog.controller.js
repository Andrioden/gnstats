function StatsDialogController($rootScope, $scope, $mdDialog, $http) {

    // *************** PUBLIC VARIABLES ***************

    $scope.loadingData = false;
    $scope.stats = undefined;
    $scope.statsBehaviorOrderByField = 'sum_weighed';
    $scope.statsBehaviorReverseSort = true;


    // *************** CONSTRUCTOR ***************

    $scope.loadingData = true;
    $http.get('/api/stats/').
        then(function (response) {
            $scope.loadingData = false;
            $scope.stats = response.data;
        }, function (response) {
            $scope.loadingData = false;
            alertError(response);
        });


    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };

    // *************** PRIVATE METHODS ***************

    console.log("StatsDialogController loaded");
}