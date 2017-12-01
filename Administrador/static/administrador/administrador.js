
(function () {
    'use strict';
    angular.module('usuario.demo', [])
        .controller('AdministradorController', ['$scope', '$http', UsuarioController]);

    function UsuarioController($scope, $http) {
        $scope.usuairo = null;
        $scope.add = function (nombre, apellido, correo, clave, direccion, celular, telefono, edad, archivo, superUsuario) {
            
            var usuario = {
                nombre: nombre, apellido:apellido, 
                correo: correo, clave:clave, direccion:direccion, celular:celular, telefono:telefono, 
                edad:edad,archivo:archivo,
                superUsuario:superUsuario,
            };
            $scope.usuairo = usuario;
            // console.log($scope.usuairo);
            // console.log($scope.data);
            $http.post('/api/administrador/', usuario)
            .then(function (response) {  
                console.log('post')  
                console.log($scope.$root.$$childHead.data);
                var usuarios = $scope.$root.$$childHead.data;
                usuarios.push(usuario);
                console.log('post-despues')  
                console.log($scope.$root.$$childHead.data);
            },
            function () {
                alert('could not create card')
            }
            );            
        }

        $scope.data = [];
        $http.get('/api/administrador/').then(function (response) {   
            //console.log();  
            console.log(response.data);
            $scope.data = response.data.results;
        });                
    }
}());
