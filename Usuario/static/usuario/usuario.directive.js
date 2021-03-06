
(function () {
    'use strict';
    angular.module('usuario.demo')
        .directive('usuarioUsuario', UsuarioDirective);

    function UsuarioDirective() {
        return {
            templateUrl: '/static/usuario/usuario.html',
            templateCss: '/static/usuario/css/usuario.css',
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http) {
                // console.log($scope)        
                // var url = '/apiusuario/usuario/'+$scope.usuario.id + '/';     

                $scope.cargar = function (usuario) {
                    $scope.id = usuario.id;
                    $scope.nombre = usuario.nombre;
                    $scope.apellido = usuario.apellido;
                    $scope.correo = usuario.correo;
                    $scope.clave = usuario.clave;
                    $scope.direccion = usuario.direccion;
                    $scope.celular = usuario.celular;
                    $scope.telefono = usuario.telefono;
                    $scope.edad = usuario.edad;
                    $scope.clave = usuario.clave;

                    var url = '/apiusuario/usuario/' + usuario.id + '/';
                    $http.put(url, usuario);
                };

                $scope.update = function (nombre, apellido, correo, clave, direccion, celular, telefono, edad, archivo) {
                    var usuario;
                    console.log("update");
                    console.log(telefono);
                    
                    console.log($scope)

                    var usuario = {
                        id: $scope.id,
                        nombre: nombre, apellido:apellido, 
                        correo: correo, clave:clave, direccion:direccion, celular:celular, telefono:telefono, edad:edad,archivo:archivo,
                    };
                    var usuarios = $scope.$root.$$childHead.data;
                    usuarios.splice(usuarios.indexOf(usuario), 1);
                    
                    console.log(usuario)
                    var url = '/apiusuario/usuario/' + usuario.id + '/';
                    $http.put(url, usuario);
                };


                $scope.delete = function (usuario) {
                    var url = '/apiusuario/usuario/' + usuario.id + '/';
                    $http.delete(url).then(
                        function () {
                            // console.log('hola')         
                            // console.log($scope.$root.$$childHead.data);
                            var usuarios = $scope.$root.$$childHead.data;
                            usuarios.splice(usuarios.indexOf(usuario), 1);
                        }
                    );
                };


                $scope.modelOptions = {
                    debounce: 500
                };
            }]
        };
    }
})();