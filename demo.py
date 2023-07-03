from fairseq.models.transformer import TransformerModel

en2vi = TransformerModel.from_pretrained(
  '/path/to/checkpoints',
  checkpoint_file='checkpoint_best.pt',
  data_name_or_path='data-bin/wmt17_zh_en_full',
  bpe='subword_nmt',
  bpe_codes='data-bin/wmt17_zh_en_full/zh.code'
)

en2vi.translate('你好 世界')