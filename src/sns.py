import some_sns_module


def send_share_sns(text: str, share: bool) -> None:
    """textに指定した文字列をとあるSNSでシェアします"""
    if share:
        some_sns_module.share(text)  # 実際にSNSに通信してほしくない
