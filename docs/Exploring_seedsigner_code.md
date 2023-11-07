# Exploring SeedSigner Code

## Export Xpub

class SeedOptionsView() <sub>[views/seed_views.py#L428](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L428)</sub>
<pre>
Displays "Export Xpub" option:

if EXPORT_XPUB selected goto SeedExportXpubSigTypeView() class [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L514">Ln 514</a>]
</pre>


class SeedExportXpubSigTypeView() [views/seed_views.py#L572](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L572)
<pre>
Displays "Single Sig" option:

if SINGLE_SIG selected goto SeedExportXpubScriptTypeView() class [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L597">Ln 597</a>]
</pre>


class SeedExportXpubScriptTypeView() [views/seed_views.py#L605](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L605)
<pre>
Displays "Native Segwit" option:

Final else statement [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L658">Ln 658</a>] is triggered if SETTING__SCRIPT_TYPES == "Native Segwit"
goto SeedExportXpubCoordinatorView() class [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L700">Ln 700</a>]
</pre>


class SeedExportXpubCoordinatorView() [views/seed_views.py#L700](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L700)
<pre>
Displays "Sparrow" option:

goto SeedExportXpubWarningView() class if any COORDINATOR select ("BlueWallet", "Nunchuk", "Sparrow" etc) [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L730">Ln 730</a>]
</pre>


class SeedExportXpubWarningView() [views/seed_views.py#L737](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L737)
<pre>
Displays "Xpub can be used to view all future transactions. I Understand" option:

goto SeedExportXpubDetailsView() class if "I Understand" selected [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L770">Ln 770</a>]
</pre>


class SeedExportXpubDetailsView() [views/seed_views.py#L779](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L779)
<pre>
Calculate xpub

goto SeedExportXpubQRDisplayView() [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L844">views/seed_views.py#L844</a>]
</pre>


class SeedExportXpubQRDisplayView() [views/seed_views.py#L856](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L856)
<pre>
runs QRDisplayScreen - the location of this class is: [<a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/gui/screens/screen.py#L659">gui/screens/screen.py#L659</a>]
</pre>

<!--
<a href=""></a>
-->