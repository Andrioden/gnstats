function AvatarDialogController($rootScope, $scope, $mdDialog, $http, $window, FileUploader) {

    // *************** PUBLIC VARIABLES ***************

    $scope.submitting = false;

    $scope.uploader = new FileUploader({
        removeAfterUpload: true,
        onAfterAddingFile: function (item) {
            item.url = "/api/users/me/avatar/";
        },
        onSuccessItem: function (item, response, status, headers) {
            $window.location.reload();
        },
        onErrorItem: function (item, response, status, headers) {
            document.getElementById("avatarFile").value = "";
            alertError(response);
        },
        onCompleteItem: function (item, response, status, headers) { },
    });


    // *************** CONSTRUCTOR ***************


    // *************** PUBLIC METHODS ***************

    $scope.cancel = function() {
        $mdDialog.cancel();
    };


    // *************** PRIVATE METHODS ***************



    console.log("AvatarDialogController loaded");
}