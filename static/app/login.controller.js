app.controller('LoginController', function($rootScope, $scope, $http){

    $http.get('/api/users/me').
        then(function(response) {
            $scope.userName = response.data.user_name;
        }, function(response) {
            alertError(response);
        });

    console.log("LoginController loaded")

});