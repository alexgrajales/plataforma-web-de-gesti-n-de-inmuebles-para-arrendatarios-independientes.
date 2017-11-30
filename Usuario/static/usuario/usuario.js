
(function () {
    'use strict';
    angular.module('usuario.demo', [])
        .controller('UsuarioController', ['$scope', '$http', UsuarioController]);

    function UsuarioController($scope, $http) {
        $scope.add = function (nombre, apellido, correo, clave, direccion, celular, telefono, edad) {
            
            var usuario = {
                nombre: nombre, apellido:apellido, 
                correo: correo, clave:clave, direccion:direccion, celular:celular, telefono:telefono, edad:edad,
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
            //console.log();  
            //console.log(response.data);
            $scope.data = response.data.results;
        });                
    }
}());
