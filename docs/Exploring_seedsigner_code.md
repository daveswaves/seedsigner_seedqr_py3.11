# Exploring SeedSigner Code

## Export Xpub

class SeedOptionsView() [views/seed_views.py#L428](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L428)
    
    Displays "Export Xpub" option:

    if EXPORT_XPUB selected goto SeedExportXpubSigTypeView() class [Ln 514](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L514)

class SeedExportXpubSigTypeView() [views/seed_views.py#L572](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L572)

    Displays "Single Sig" option:

    if SINGLE_SIG selected goto SeedExportXpubScriptTypeView() class [Ln 597](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L597)

class SeedExportXpubScriptTypeView() [views/seed_views.py#L605](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L605)

    Displays "Native Segwit" option:

    Final else statement [Ln 658] is triggered if SETTING__SCRIPT_TYPES == "Native Segwit"  
    goto SeedExportXpubCoordinatorView() class [Ln 700](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L700)

class SeedExportXpubCoordinatorView() [views/seed_views.py#L700](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L700)

    Displays "Sparrow" option:

    goto SeedExportXpubWarningView() class if any COORDINATOR select ("BlueWallet", "Nunchuk", "Sparrow" etc) [Ln 730](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L730)

class SeedExportXpubWarningView() [views/seed_views.py#L737](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L737)

    Displays "Xpub can be used to view all future transactions. I Understand" option:

    goto SeedExportXpubDetailsView() class if "I Understand" selected [Ln 770](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L770)

class SeedExportXpubDetailsView() [views/seed_views.py#L779](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L779)

<pre>
Calculate xpub

goto SeedExportXpubQRDisplayView() <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L844">views/seed_views.py#L844</a>
</pre>

class SeedExportXpubQRDisplayView() [views/seed_views.py#L856](https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/views/seed_views.py#L856)

<pre>runs QRDisplayScreen - the location of this class is: <a href="https://github.com/SeedSigner/seedsigner/blob/dev/src/seedsigner/gui/screens/screen.py#L659">gui/screens/screen.py#L659</a></pre>