<!--todo: refactor title; it's confusing-->
% rebase('base.tpl', title='Chani - '+title)

<h1>{{title}}</h1>
%if len(items) == 0:
  <h3>No se encontraron coincidencias para "{{q}}".</h3>
%else:
  %if defined('q'):
    <h3>Coincidencias para "{{q}}":</h3>
  %end
  <table class="table table-bordered table-striped table-hover">
    <tr>
      <th>name</th>
      <th>quantity</th>
      <th>unit</th>
      <th>price</th>
      <th>currency</th>
      <th>place</th>
      <th>date</th>
    </tr>
    % for i in items:
      <tr>
        <td>{{i.name}}</td>
        <td>{{i.quantity}}</td>
        <td>{{i.unit}}</td>
        <td>{{i.price}}</td>
        <td>{{i.currency}}</td>
        <td>{{i.place}}</td>
        <td>{{i.date}}</td>
      </tr>
    % end
  </table>
%end
<a href="/">Regresar</a>
