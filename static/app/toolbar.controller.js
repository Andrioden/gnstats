app.controller('ToolbarController', function($rootScope, $scope, $http, $window, $mdDialog){


    // *************** PUBLIC VARIABLES ***************

    $rootScope.loadingUsers = false;
    $rootScope.users = [];
    $rootScope.user = {
        google_email: "",
        person: false
    };


    // *************** CONSTRUCTOR ***************

    $http.get('/api/users/me/').
        then(function(response) {
            $rootScope.user = response.data;
        }, function(response) {
            alertError(response);
        });

    $rootScope.loadingUsers = true;
    $http.get('/api/users/').
        then(function(response) {
            $rootScope.users = response.data;
            $rootScope.loadingUsers = false;
        }, function (response) {
            $rootScope.loadingUsers = false;
            alertError(response);
        });


    // *************** PUBLIC METHODS ***************

    $scope.openVerificationDialog = function (ev) {
        $mdDialog.show({
            controller: VerificationDialogController,
            templateUrl: 'static/app/toolbar-extra.verificationDialog.template.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true,
            fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
        })
        // Hidden with potential return value
        .then(function (deletedTrueOrGameNightObject) {
        },
        // Cancelled
        function () { });
    };

    $scope.openAdminDialog = function (ev) {
        $mdDialog.show({
            controller: AdminDialogController,
            templateUrl: 'static/app/toolbar-extra.adminDialog.template.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true,
            fullscreen: $scope.customFullscreen // Only for -xs, -sm breakpoints.
        })
        // Hidden with potential return value
        .then(function () {},
        // Cancelled
        function () { });
    };

    $scope.openStatsDialog = function (ev) {
        $mdDialog.show({
            controller: StatsDialogController,
            templateUrl: 'static/app/toolbar-extra.statsDialog.template.html',
            parent: angular.element(document.body),
            targetEvent: ev,
            clickOutsideToClose: true,
            fullscreen: true // Only for -xs, -sm breakpoints.
        })
        // Hidden with potential return value
        .then(function () { },
        // Cancelled
        function () { });
    };

    $scope.openCreateNewGameNightDialog = function (ev) {
        $rootScope.$emit('openGameNightDialog', {ev: ev, gameNight: null});
    };

    
    // *************** PRIVATE METHODS ***************


    console.log("ToolbarController loaded");
});