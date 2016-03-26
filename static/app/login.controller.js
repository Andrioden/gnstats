app.controller('LoginController', function($rootScope, $scope, $http, $window){


    // *************** PUBLIC VARIABLES ***************
    $rootScope.user = {
        nickname: "",
        verified: false
    }
    $scope.personNames = ['Stian', 'André', 'Ole', 'Damian'];
    $scope.password = "";


    // *************** CONSTRUCTOR ***************

    $http.get('/api/users/me/').
        then(function(response) {
            $rootScope.user = response.data;
        }, function(response) {
            alertError(response);
        });

    console.log("LoginController loaded")

    // *************** PUBLIC METHODS ***************

    $scope.verify = function() {
        console.log($rootScope.user)
        $http.post('/api/users/verify/', {name: $rootScope.user.name, nickname: $rootScope.user.nickname, password: $scope.password}, {}).
            then(function(response) {
                $rootScope.user.verified = true;
                $("#verifyModal").modal("hide");
                $window.location.reload();
            }, function(response) {
                alertError(response);
            });
    }


    // *************** PRIVATE METHODS ***************

});