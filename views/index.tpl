  <head>
    <title> Task Manager </title>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="static/styles.css">
  </head>

  <body>
    <h1> Simple Task Manager </h1>
    <ul id="todo-list"> </ul>
    % for task in tasks:
    <li>
      <input class="checkbox" type="checkbox"/>
      {{ task.description}}
      <a class="remove" href="#">×</a>
      <hr/>
    </li>
    %end
    <br/>
    <form id="todo-add">
      <input type="text" class="form-control"/>
      <button class="add" type="submit">+</button>
    </form>
  </body>

</html>
