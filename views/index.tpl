<html>
  <head>
    <title>Today tasks</title>
    <link rel="stylesheet" href="static/styles.css">
    <script src="http://code.jquery.com/jquery-3.3.1.min.js"></script>
    <script src="static/script.js"></script>
  </head>

  <body>
    <div class="container">
    <h1>Tasks</h1>
    <ul id="todo-list">
    % for task in tasks:
      % if task.is_completed:
        <li class="completed">
          <input class='checkbox' data-uid={{ task.uid }} type='checkbox'
          disabled='disabled' checked='checked'/>
        % else:
        <li>
          <input class='checkbox' data-uid={{ task.uid }} type='checkbox' />
        % end
        {{ task }}
        <a class="remove" href="/api/delete/{{ task.uid }}">X</a>
        <hr/>
        </li>
      % end
      </ul>
      <form id="todo-add">
        <input type="text" id="new-todo-description" class="form-control"/>
        <button class="add" type="submit">+</button>
      </form>
    </div>
  </body>
</html>
