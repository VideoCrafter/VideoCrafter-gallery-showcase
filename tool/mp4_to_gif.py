import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(video_path, out_path, savefps):
    videoClip = VideoFileClip(video_path)
    videoClip.write_gif(out_path, fps=savefps)

def convert_mp4_folder_to_gif(video_dir, out_dir, savefps):
    video_paths = sorted([os.path.join(video_dir, vname) for vname in os.listdir(video_dir) if vname.endswith('.mp4') or vname.endswith('.mov')])
    for video_path in video_paths:
        videoClip = VideoFileClip(video_path)
        # videoClip = videoClip.resize(width=1500)
        video_name = os.path.basename(video_path).split('.mp4')[0] + ".gif"
        print(video_name)
        videoClip.write_gif(os.path.join(out_dir, video_name), fps=savefps)

if __name__ == "__main__":
    # video dir
    video_dir = "./assets/lora/mp4_file/"
    out_dir = video_dir + "_GIF"
    savefps = 8
    
    

    os.makedirs(out_dir, exist_ok=True)
    convert_mp4_folder_to_gif(video_dir, out_dir, savefps)

    # single video
    # video_path="/Users/heyingqing/text2vid_results/gallery/category-basedon-exp/v8-lora-models/2-frozen/magicvideo_mini/024_overlap_t_0_prompt_2_UncondScale_15.0_32x16x256x256x3-samples.mp4"
    # out_path=video_path.split('.')[0] + '.gif'
    # savefps = 8
    # convert_mp4_to_gif(video_path, out_path, savefps)