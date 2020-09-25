#!/usr/bin/node
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('INPUT#btn_translate').click(() => {
    const param = 'lang=' + $('INPUT#language_code').val();
    $.get(url + param, (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
