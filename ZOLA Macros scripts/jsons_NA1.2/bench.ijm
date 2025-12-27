dir = "/home/syan/bench/";
fileList = getFileList(dir);

for (i = 0; i < fileList.length/3; i++) {
    print(fileList[3*i]);
    open(dir+fileList[3*i]);
    open(dir+fileList[3*i+1]);
    open(dir+fileList[3*i+2]);
	run("Images to Stack", "use");
	makeRectangle(0, 0, 64, 64);
	run(" Calibration: PSF modeling", "  gain=1 pixel_size=106 z_step=40 bead_moving=[far -> close to objective] numerical_aperture=1.200 immersion_refractive=1.000 wavelength=1.070 patch_size=64 zernike_coefficient=[Zernike 15 coefs] iteration=30 result_calibration_file=/home/syan/json_bench/"+d2s(i, 0)+".json");
	close();
	close();
	selectImage("Stack");
	close();
}