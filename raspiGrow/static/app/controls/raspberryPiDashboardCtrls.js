var raspberryPiDashboardCtrls = angular.module('raspberryPiDashboardCtrls', []);

raspberryPiDashboardCtrls.controller('raspberryPiDashboardCtrls', ['$scope', '$http', 'statusMapService',

  function ($scope, $http) {
      $http.get('phones/phones.json').success(function(data) {
          $scope.phones = data;
      });
    
      $scope.orderProp = 'age';
  }]);

raspberryPiDashboardCtrls.controller('raspberryPiDashboardCtrls', ['$scope', '$routeParams', 'statusMapService',

  function ($scope, $routeParams, statusMapService) {
      var vm = this;
      vm.statusMap = statusMapService.statusMap;

      var degreesSymbol = '\u00B0';
      $scope.temp = '70' + degreesSymbol + ' F';
      $scope.actTemp = 70.0;
      $scope.actHumidity = 50;
      $scope.humidity = '40% RH';
      $scope.statusTopLights = true;
      $scope.statusBottomLights = true;
      $scope.statusTopFan = true;
      $scope.statusBottomFan = true;
      $scope.phoneId = $routeParams.phoneId;
      $scope.changeTopLightStatus = function () {
          $scope.statusTopLights = !$scope.statusTopLights;
         
      }
      $scope.changeBottomLightStatus = function () {
          $scope.statusBottomLights = !$scope.statusBottomLights;

      }
      $scope.changeBottomFanStatus = function () {
          $scope.statusBottomFan = !$scope.statusBottomFan;

      }
      $scope.changeTopFanStatus = function () {
          $scope.statusTopFan = !$scope.statusTopFan;

      }
  }]);