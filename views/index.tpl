% rebase('base.tpl', title='Chani')
<!--change this shit so it doesn't do an unnecessary post-->
<form role="form" action="/item/new" method="post">
  <div class="jumbotron">
  <h1>Bienvenido a Chani!</h1>
  <h2>Buscar o Registrar</h2>
  <div class="form-group">
  <input type="text" class="form-control" name="newItemExp" autofocus/>
  </div>
  <!--must be outside form-group so it's not sticking to the form"-->
  <input type="submit" class="btn btn-primary" value="Consultar" />
  </div>
</form>
