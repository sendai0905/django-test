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
