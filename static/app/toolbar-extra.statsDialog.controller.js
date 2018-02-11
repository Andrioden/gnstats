function StatsDialogController($rootScope, $scope, $mdDialog, $http, $window) {

    // *************** PUBLIC VARIABLES ***************

    $scope.loadingData = false;
    $scope.stats;
    $scope.statsBehaviorOrderByField = 'sum';
    $scope.statsBehaviorReverseSort = true;


    // *************** CONSTRUCTOR ***************

    $scope.loadingData = true;
    $http.get('/api/actions/stats/').
        then(function (response) {
            $scope.loadingData = false;
            console.log(response);
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