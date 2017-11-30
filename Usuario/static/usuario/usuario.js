
(function () {
    'use strict';
    angular.module('usuario.demo', [])
        .controller('UsuarioController', ['$scope', '$http', UsuarioController]);

    function UsuarioController($scope, $http) {
        $scope.add = function (nombre, correo, clave, direccion) {
            
            var usuario = {
                nombre: nombre,
                correo: correo, clave:clave, direccion:direccion
            };
            $http.post('/apiusuario/usuario/', usuario)
            .then(function (response) {                
            },
            function () {
                alert('could not create card')
            }
            );            
        }

        $scope.data = [];
        $http.get('/apiusuario/usuario/').then(function (response) {   
            // console.log("get");  
            // console.log(response.data);
            $scope.data = response.data.results;
        });                
    }
}());
