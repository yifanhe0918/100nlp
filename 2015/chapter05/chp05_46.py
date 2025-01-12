"""
46. 動詞の格フレーム情報の抽出

45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
"""

import chp05_45 as p45

if __name__ == '__main__':
    verbcase_pats = p45.main()
    for verbcase_pat in verbcase_pats:
        for verb, src_chunks in verbcase_pat:
            col1 = verb.morphs_of_pos('動詞')[-1].base
            # sorted(src_chunks)
            col2_3 = [(src_chunk.morphs_of_pos1('格助詞')[-1].base, str(src_chunk)) for src_chunk in src_chunks]
            sorted_col2_3 = sorted(col2_3, key=lambda x: x[0])
            col2 = " ".join([i[0] for i in sorted_col2_3])
            col3 = " ".join([i[1] for i in sorted_col2_3])
            print(col1, col2, col3, sep='\t')
