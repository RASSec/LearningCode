<?php
class test1
{
    private $test1_data = 'test1_data';
    private $test1_filename = './test1_demo.txt';
    public function __construct()
    {
        $this->save($this->test1_filename);
    }
    public function save($test1_filename)
    {
        file_put_contents($test1_filename, $this->test1_data);
    }
}