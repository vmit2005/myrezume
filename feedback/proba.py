from re import findall
sstr="""<tr>
    <th><label for="id_title">Тема сообщения:</label></th>
    <td>

      <input type="text" name="title" value="ww" class="form-control" placeholder="Тема" maxlength="255" required id="id_title">


    </td>
  </tr>

  <tr>
    <th><label for="id_author">Автор:</label></th>
    <td>

      <input type="text" name="author" value="www" class="form-control2" placeholder="Автор" maxlength="255" id="id_author">


    </td>
  </tr>

  <tr>
    <th><label for="id_mail">E-mail:</label></th>
    <td>

      <input type="text" name="mail" value="wwww" class="form-control2" placeholder="e-mail" maxlength="255" id="id_mail">


    </td>
  </tr>

  <tr>
    <th><label for="id_description">Сообщение:</label></th>
    <td>

      <textarea name="description" cols="40" rows="5" class="form-control" placeholder="Текст сообщения" id="id_description">
wwwww</textarea>




    </td>
  </tr>
"""
def form_sort(str(sstr)):
    patt = r'value=\S+'
    a=findall(patt,sstr)
    a0=a[0][7:-1]
    a1=a[1][7:-1]
    a2=a[2][7:-1]
    patt=r'>\s+.+</textarea'
    a=findall(patt,sstr)
    b=a[0][2:-10]
    return (a0,a1,a2,b)
print(form_sort(sstr))