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

    public static function dispatch() {
        $path = Request::getPath()[0];

        if (isset($_SESSION['init'])) {
          echo '<script>localStorage.removeItem("startDate");</script>';
          unset($_SESSION['init']);
        }

        if ($path === 'debug') {
            self::_debug();
            return;
        }

        Response::put('index.html');
    }
}
