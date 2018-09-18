# import youtube_dl
# import progressbar
# import shutil
# import main


class download():
    def pb_hook(d):
        if d['status'] == 'finished':
            columns = shutil.get_terminal_size().columns
            # print("++ List Video Format ++\n\n\n".center(columns))
            print("\n")
            print("Done downloading {}".format(d['filename']).center(columns))
            main.pilihan()
        if d['status'] == 'downloading':
            show_progress(d['downloaded_bytes'], d['total_bytes'])


    pbar = None
    def show_progress(downloaded, total_size):
        widgets = [
            ' [', progressbar.AdaptiveTransferSpeed(), '] ',
            progressbar.Bar(),
            ' (', progressbar.DataSize(), ') ', "(", progressbar.Percentage(), ")",
        ]

        global pbar
        if (pbar is None):
            pbar = progressbar.ProgressBar(maxval=total_size, widgets=widgets)

        if downloaded < total_size:
            pbar.update(downloaded)
        else:
            pbar.finish()
            pbar = None

