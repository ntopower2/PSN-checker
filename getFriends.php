<?php
require_once 'vendor/autoload.php';

use PlayStation\Client;

$client = new Client();
$client->loginWithNpsso('jP5acDu3NQ2t6m2odynCojrIK7fSkiuJ46ftPJQuV7WQGeSiODR1OgUCFiAaDc1P');

$refreshToken = $client->refreshToken();
$username = $argv[1];
if (count($argv) == 1) {
    echo "No username given. Exiting..";
    return 0;
}
elseif (count($argv) == 2) {
    $upperlimit = 250;
}
elseif (is_numeric($argv[2]) & $argv[2] > 0 & $argv[2] < 2001) {
    $upperlimit = $argv[2];
}
else {
    echo "Undefined argument error. Exiting..";
    return 0;
}
$me = $client->user($username);
$friends = $me->friends('onlineStatus',0,$upperlimit);
//$fp = fopen("friendslist_".$username.".txt","w");

foreach ($friends as $friend) {
    //fwrite($fp,$friend->onlineId());
    //fwrite($fp,"\n");
    echo $friend->onlineId()."\n";
}
//fclose($fp);