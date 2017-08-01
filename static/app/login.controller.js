app.controller('LoginController', function($rootScope, $scope, $http, $window){


    // *************** PUBLIC VARIABLES ***************
    $rootScope.persons = [];
    $rootScope.user = {
        nickname: "",
        verified: false
    }
    $scope.availablePersonNames = ['Loading...'];
    $scope.password = "";


    // *************** CONSTRUCTOR ***************

    $http.get('/api/users/my/').
        then(function(response) {
            $rootScope.user = response.data;
        }, function(response) {
            alertError(response);
        });

    $http.get('/api/users/').
        then(function(response) {
            $rootScope.persons = response.data;
        }, function(response) {
            alertError(response);
        });

    $http.get('/api/users/available-names/').
        then(function(response) {
            $scope.availablePersonNames = response.data;
        }, function(response) {
            alertError(response);
        });

    console.log("LoginController loaded")

    // *************** PUBLIC METHODS ***************

    $scope.verify = function() {
        console.log($rootScope.user)
        $http.post('/api/users/verify/', {name: $rootScope.user.name, password: $scope.password}, {}).
            then(function(response) {
                $rootScope.user.verified = true;
                $("#verifyModal").modal("hide");
                $window.location.reload();
            }, function(response) {
                alertError(response);
            });
    }

    $scope.activate = function(person) {
        $http.post('/api/users/activate/', {name: person.name}, {}).
            then(function(response) {
                console.log(response);
            }, function(response) {
                alertError(response);
            });
    }

    $scope.deactivate = function(person) {
        $http.post('/api/users/deactivate/', {name: person.name}, {}).
            then(function(response) {
                console.log(response);
            }, function(response) {
                alertError(response);
            });
    }

    // *************** PRIVATE METHODS ***************


});