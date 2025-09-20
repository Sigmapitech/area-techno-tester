<?php

namespace demo\core;

class Application extends Dispatcher
{
    private static function _debug()
    {
        echo '<pre>';
        var_dump($GLOBALS);
        echo '</pre>';
    }

    public static function _notFound() {
        Response::status(404);
        Response::json(['error' => 'Not found']);
    }

    public static function _forbidden() {
        Response::status(403);
        Response::json(['error' => 'Forbidden']);
    }

    public static function dispatch() {
        $params = Request::getPath();

        if ($params[0] === 'debug') {
            self::_debug();
            return;
        }

        array_shift($params);

        $rawEndpoint = array_shift($params);

        if ($rawEndpoint === null || $rawEndpoint === '') {
            readfile('index.html'); 
            return;
        }

        $endpointName = ucfirst($rawEndpoint);
        $endpointPath = 'api/' . $endpointName . '.php';

        if (!file_exists($endpointPath)) {
            self::_notFound();
            return;
        }

        require_once $endpointPath;
        $endpoint = new $endpointName();

        $method = Request::getMethod();

        $func_name = array_shift($params);
        if ($func_name === null) {
            self::_notFound();
            return;
        }

        $action = $method . ucfirst($func_name);

        if (!method_exists($endpoint, $action)) {
            self::_notFound();
            return;
        }

        Response::status(200);
        Response::json($endpoint->$action() ?? []);
    }
}
