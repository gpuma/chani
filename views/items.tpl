<!--todo: refactor title; it's confusing-->
% rebase('base.tpl', title='Chani - '+title)

<h2>{{get('q',title)}}</h2>
<table>
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
<a href="/">Regresar</a>
