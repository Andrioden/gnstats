app.controller('LoginController', function($rootScope, $scope, $http){


    // *************** PUBLIC VARIABLES ***************
    $rootScope.user = {
        nickname: "",
        verified: false
    }
    $scope.personNames = ['Stian', 'André', 'Ole', 'Damian'];
    $scope.password = "";


    // *************** CONSTRUCTOR ***************

    console.log("LoginController loaded")

    $http.get('/api/users/me/').
        then(function(response) {
            $rootScope.user = response.data;
        }, function(response) {
            alertError(response);
        });

    // *************** PUBLIC METHODS ***************

    $scope.verify = function() {
        console.log($rootScope.user)
        $http.post('/api/users/verify/', {name: $rootScope.user.name, nickname: $rootScope.user.nickname, password: $scope.password}, {}).
            then(function(response) {
                $rootScope.user.verified = true;
                $("#verifyModal").modal("hide");
            }, function(response) {
                alertError(response);
            });
    }


    // *************** PRIVATE METHODS ***************

});