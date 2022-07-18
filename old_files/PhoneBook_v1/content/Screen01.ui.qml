/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import PhoneBook_v1

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello PhoneBook_v1")
        anchors.centerIn: parent
        font.family: Constants.font.family
    }

    Image {
        id: image
        x: 34
        y: 72
        width: 136
        height: 126
        source: "../../images/add-contact.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: image1
        x: 412
        y: 72
        width: 128
        height: 126
        source: "../../images/close.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: image2
        x: 238
        y: 72
        width: 118
        height: 126
        source: "../../images/email.png"
        fillMode: Image.PreserveAspectFit
    }

    Button {
        id: button
        x: 42
        y: 72
        width: 120
        height: 126
        visible: false
        text: qsTr("Button")
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}D{i:3}
}
##^##*/
