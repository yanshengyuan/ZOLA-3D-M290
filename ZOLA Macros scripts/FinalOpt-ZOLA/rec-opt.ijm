dir = "/home/syan/rec/";
fileList = getFileList(dir);

for (i = 0; i < fileList.length/3; i++) {
    print(fileList[3*i]);
    open(dir+fileList[3*i]);
    open(dir+fileList[3*i+1]);
    open(dir+fileList[3*i+2]);
    run("Images to Stack", "use");
    makePoint(32, 32, "small yellow hybrid");
    run(" Calibration: PSF modeling", "  gain=1 pixel_size=106 z_step=2000 bead_moving=[close -> far from objective] numerical_aperture=1.500 immersion_refractive=1.600 wavelength=1.070 patch_size=64 zernike_coefficient=[Zernike 15 coefs] iteration=30 result_calibration_file=/home/syan/json_rec/"+d2s(i, 0)+".json");
    selectImage("input-model image ");
    saveAs("Tiff", "/home/syan/psf_rec/" +d2s(i, 0)+ ".tif");
    close();
    selectImage("phase");
    saveAs("PNG", "/home/syan/phase_rec/" +d2s(i, 0)+ ".png");
    close();
    selectImage("Stack");
    close();
}