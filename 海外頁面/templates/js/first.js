// Code goes here

var app = angular.module("app1",[]);

app.controller("LangController",["$scope", function($scope){
  $scope.langs = ["華語", "閩語", "客語"];
  $scope.call = function(lang){
    alert(lang);
  };
}]);