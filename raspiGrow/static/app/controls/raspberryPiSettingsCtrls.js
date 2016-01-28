var raspberryPiSettingsCtrls = angular.module('raspberryPiSettingsCtrls', []);

raspberryPiSettingsCtrls.controller('raspberryPiSettingsCtrls', ['$scope', '$http',
  function ($scope, $http) {
      $http.get('phones/phones.json').success(function(data) {
          $scope.phones = data;
      });

      $scope.orderProp = 'age';
  }]);

raspberryPiSettingsCtrls.controller('raspberryPiSettingsCtrls', ['$scope', '$routeParams',
  function($scope, $routeParams) {
      $scope.phoneId = $routeParams.phoneId;
  }]);