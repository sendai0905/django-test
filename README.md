# TODO

- [x] html 装飾
      css をパクった
- [ ] category によるクエリ検索(集計)
- [x] 記事投稿フォーム実装

  - CreateView は ModelFormMixin を継承しているので form_valid を指定しなくてもよい
  - 指定した場合はオーバーライドという形になるので返り値として super().form_valid(form)という形で指定するとうまく httpresponse で返ってくる

- [ ] 時刻アーカイブ(集計)
- [ ] 記事検索
- [x] /article/<int:pk>/で記事単体を表示させる
- [x] 記事の削除

  - DeleteView

- [x] html タグが使えるようにする
      {{ article.detail | safe }}
- [x] 改行がきくようにする
      {{ article.detail | linebreaksbr }}
- [ ] 画像を挿入できるようにする

# メモ

## 気づき

- view と紐付いていないモデルのデータを引っ張ってくる

  ```python
  @property
  def test(self):
    return Unko.objects.get(id=1)
  ```

  みたいな感じで、html は

  ```html
  {{ test }}
  ```

  でデータを引っ張ってこれる

## genericview について

### 継承元

- TemplateView
  - TemplateResponseMixin
    - render_to_response  
       このビューの `response_class`を使用して、指定されたコンテキストでレンダリングされたテンプレートで応答を返します。  
            response_kwargs を応答クラスのコンストラクターに渡します。
    - get_template_names  
      リクエストに使用されるテンプレート名のリストを返します。リストを返す必要があります。 render_to_response（）がオーバーライドされている場合は呼び出されません。
  - ContextMixin
    get_context_data（）が受け取ったキーワード引数をテンプレートコンテキストとして渡すデフォルトのコンテキストミックスイン。
    - get_context_data
  - View  
    たくさん
- DetailView  
   オブジェクトの「詳細」ビューをレンダリングします。  
        デフォルトでは、これは `self.queryset`からルックアップされたモデルインスタンスですが、  
       view は、 `self.get_object（）`をオーバーライドすることにより、* any *オブジェクトの表示をサポートします。
  - SingleObjectTemplateResponseMixin
    - get_template_names (override)  
       リクエストに使用されるテンプレート名のリストを返します。 render_to_response（）がオーバーライドされている場合は呼び出されません。次のリストを返します。  
              *ビューの `template_name`の値（提供されている場合）  
              *ビューが操作しているオブジェクトインスタンスの `template_name_field`フィールドの内容（利用可能な場合）  
              \* `<app_label> / <model_name> <template_name_suffix> .html`
    - TemplateResponseMixin
  - BaseDetailView
- ListView
- FormView
- CreateView
- UpdateView
- DeleteView
