import pygame
# Some versions of pygame lack text direction constants required by pygame_gui.
if not hasattr(pygame, "DIRECTION_LTR"):
    pygame.DIRECTION_LTR = 0
    pygame.DIRECTION_RTL = 1

if not hasattr(pygame, "FRect"):
    pygame.FRect = pygame.Rect

if not hasattr(pygame, "Event"):
    pygame.Event = pygame.event.Event

import pygame_gui
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent / "assets"


class GUIApp:
    """Simple pygame_gui-based interface with a text box and button."""

    def __init__(self, width: int = 800, height: int = 600) -> None:
        pygame.init()
        pygame.display.set_caption("Voidbound GUI")
        self.window_surface = pygame.display.set_mode((width, height))
        self.background = pygame.Surface((width, height))
        self.background.fill((30, 30, 30))
        self.manager = pygame_gui.UIManager((width, height))

        icon_path = ASSETS_DIR / "placeholder.png"
        if icon_path.exists():
            try:
                icon = pygame.image.load(icon_path).convert_alpha()
                pygame.display.set_icon(icon)
            except pygame.error:
                pass

        self.output_box = pygame_gui.elements.UITextBox(
            html_text="<b>Welcome to Voidbound!</b>",
            relative_rect=pygame.Rect((20, 20), (width - 40, height - 120)),
            manager=self.manager,
        )
        self.text_entry = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect((20, height - 60), (width - 140, 40)),
            manager=self.manager,
        )
        self.send_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((width - 110, height - 60), (90, 40)),
            text="Send",
            manager=self.manager,
        )

        self.clock = pygame.time.Clock()
        self.running = True

    def run(self) -> None:
        """Run the main GUI loop."""

        while self.running:
            time_delta = self.clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if (
                    event.type == pygame_gui.UI_BUTTON_PRESSED
                    and event.ui_element == self.send_button
                ):
                    text = self.text_entry.get_text()
                    if text:
                        self.output_box.append_html_text(f"<br>{text}")
                        self.text_entry.set_text("")
                self.manager.process_events(event)

            self.manager.update(time_delta)
            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()


def main() -> None:
    GUIApp().run()


if __name__ == "__main__":
    main()
