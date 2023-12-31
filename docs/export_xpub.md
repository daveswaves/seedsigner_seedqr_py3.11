# Export Xpub Animated QR-Code

Required Scripts:
* [helpers/qr.py](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/qr.py)
* [tests/test_seedqr.py](https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_seedqr.py)
* [models/encode_qr.py](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py)
* [gui/screens/seed_screens.py](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/gui/screens/seed_screens.py)
* [tests/test_encodepsbtqr.py](https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py)
* [views/psbt_views.py](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/psbt_views.py)
* [views/tools_views.py](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/tools_views.py)
* [views/seed_views.py](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py)

<pre>
QR.qrimage() <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/qr.py#L15">15</a> and QR.qrimage_io() <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/helpers/qr.py#L39">39</a> are referenced in the following:

* tests/test_seed_qr.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_seedqr.py#L25">25</a> (qrimage)
* models/encode_qr.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L128">128</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L130">130</a> (qrimage / qrimage_io)
* gui/screens/seed_screens.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/gui/screens/seed_screens.py#L1117">1117</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/gui/screens/seed_screens.py#L1152">1152</a> (qrimage / qrimage)
</pre>

<pre>
EncodeQR <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L25">25</a> is referenced in the following:

* tests/test_encodepsbtqr.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L15">15</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L30">30</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L66">66</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L77">77</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L86">86</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_encodepsbtqr.py#L98">98</a>
* tests/test_seedqr.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/tests/test_seedqr.py#L20">20</a>
* views/psbt_views.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/psbt_views.py#L501">501</a>
* views/tools_views.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/tools_views.py#L698">698</a>
* views/seed_views.py <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L880">880</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L1389">1389</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L1424">1424</a> <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L2067">2067</a>
</pre>

## NOTES

If qr_type is 'Xpub' [[models/encode_qr.py#L63](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L63)] in the `EncodeQR` class, call `XpubQrEncoder()` method and assign result to self.encoder.

`EncodeQR.next_part_image()` [[125](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/models/encode_qr.py#L125)] is only referenced once (`QRDisplayScreen` class) - `gui/screens/screen.py` [[754](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/gui/screens/screen.py#L754)]


