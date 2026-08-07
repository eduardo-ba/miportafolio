import type { TranslationKey } from "../i18n";

/**
 * Datos que no dependen del idioma: URLs, correo, enlaces de verificación.
 * Los textos visibles viven en `src/i18n/*.json`; aquí solo se referencian por clave.
 */

export const email = "leduardobarron@gmail.com";

/** Igual en los tres idiomas, así que es dato y no traducción. */
export const location = "Mazatlán, MX";

export const social = {
	github: "https://github.com/eduardo-ba",
	linkedin: "https://www.linkedin.com/in/luis-eduardo-barron-alvarez-60082b387/",
} as const;

export const cvPath = "/cv-luis-eduardo-barron.pdf";

export interface Certification {
	/** Clave en los diccionarios i18n. */
	labelKey: TranslationKey;
	/** Enlace de verificación del emisor. */
	url: string;
	issuer: "Cisco Networking Academy" | "Capacítate para el Empleo";
}

export const certifications: Certification[] = [
	{
		labelKey: "cert_ccna_srwe",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/certificates/?issuanceId=a9c7ddd7-4098-4be4-a2b0-e318a508dbfd",
	},
	{
		labelKey: "cert_ccna_itn",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/es/certificates?issuanceId=6124782b-c283-44a3-bdda-66d200ac890b",
	},
	{
		labelKey: "cert_net_basics",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/es/certificates?issuanceId=f88efae3-44d1-4b58-9697-d2402b0293ca",
	},
	{
		labelKey: "cert_linux",
		issuer: "Cisco Networking Academy",
		url: "https://www.netacad.com/es/certificates?issuanceId=2fbc2b89-6d3f-4410-88c4-f23aee7c4dc2",
	},
	{
		labelKey: "cert_server_admin",
		issuer: "Capacítate para el Empleo",
		url: "https://capacitateparaelempleo.org/verifica/c0dc2a1a-48ff-4f41-bbba-fa27d0166de7/36dbbe32-abce-4f55-8330-b4a819841fc5",
	},
	{
		labelKey: "cert_cabling",
		issuer: "Capacítate para el Empleo",
		url: "https://capacitateparaelempleo.org/verifica/c0dc2a1a-48ff-4f41-bbba-fa27d0166de7/0832df80-f62a-46bb-b47a-fc5ebbdad964",
	},
];

export interface SkillGroup {
	titleKey: TranslationKey;
	items: string[];
}

/**
 * §15: nada de píldoras de colores. Los nombres son el contenido; el orden
 * dentro de cada grupo va de más a menos usado, no alfabético.
 */
export const skills: SkillGroup[] = [
	{
		titleKey: "skills_lang_title",
		items: ["Python", "Java", "JavaScript", "Kotlin", "C", "C++", "HTML", "CSS"],
	},
	{
		titleKey: "skills_fw_title",
		items: ["Node.js", "React", "Android SDK", "OpenCV"],
	},
	{
		titleKey: "skills_db_title",
		items: ["MySQL", "SQLite", "Firebase"],
	},
	{
		titleKey: "skills_tools_title",
		items: ["Cisco Packet Tracer", "GitHub", "GitLab", "VS Code", "Android Studio"],
	},
];

export interface Project {
	titleKey: TranslationKey;
	descKey: TranslationKey;
	techKey: TranslationKey;
	repo: string;
}

export const projects: Project[] = [
	{
		titleKey: "p1_title",
		descKey: "p1_desc",
		techKey: "p1_tech_list",
		repo: "https://github.com/eduardo-ba/red-CETIS127",
	},
	{
		titleKey: "p2_title",
		descKey: "p2_desc",
		techKey: "p2_tech_list",
		repo: "https://github.com/eduardo-ba/packet-tracer-practicas",
	},
];
