app.controller('LoginController', function($rootScope, $scope, $http){


    // *************** PUBLIC VARIABLES ***************
    $scope.nickname = "";
    $scope.password = "";
    $scope.verified = false;


    // *************** CONSTRUCTOR ***************

    console.log("LoginController loaded")

    $http.get('/api/users/me/').
        then(function(response) {
            $scope.nickname = response.data.nickname;
            $scope.verified = response.data.verified;
        }, function(response) {
            alertError(response);
        });

    // *************** PUBLIC METHODS ***************

    $scope.verify = function() {
        $http.post('/api/users/verify/', {nickname: $scope.nickname, password: $scope.password}, {}).
            then(function(response) {
                $scope.verified = true;
                $("#verifyModal").modal("hide");
            }, function(response) {
                alertError(response);
            });
    }


    // *************** PRIVATE METHODS ***************

});